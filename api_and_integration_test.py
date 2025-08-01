from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
from configs import *
import json
import os
from convert_word import WordConverter

class CT:
    def __init__(self, module_name:str, urls:list) -> None:
        self.module_name = module_name
        self.urls = urls
        self.executed_tests = []                                # 記錄哪些測試已經運行過

    def run_single_test(self, key, value, delay=3000):
        """執行單個 Postman 測試 (讓 ThreadPoolExecutor 併發呼叫)"""
        os.makedirs("html", exist_ok=True)
        os.makedirs("json", exist_ok=True)
        os.makedirs("docx", exist_ok=True)

        html_file_path = os.path.join("html", f'report_{self.module_name}_{key}.html')
        json_file_path = os.path.join("json", f'report_{self.module_name}_{key}.json')


        # 產生獨立環境變數 JSON
        env_file = f"env_{self.module_name}_{key}.json"
        env_content = {
            "id": key,
            "api_key": f"API_KEY_FOR_{key}",  # 為每個測試 Collection 設定不同 API 金鑰
            "session_token": f"TOKEN_{key}",  # 讓每個測試使用獨立 Session
            "base_url": "https://api.example.com"
        }
        with open(env_file, "w") as f:
            json.dump(env_content, f)

        command = [
            "newman", "run", value,
            "--reporters", "cli,htmlextra,json",
            "--reporter-htmlextra-export", html_file_path,
            "--reporter-htmlextra-title", f"CT {self.module_name}",
            "--reporter-htmlextra-timezone", "Asia/Taipei",
            "--reporter-json-export", json_file_path,
            "--delay-request", str(delay),
            "-e", env_file  # ✅ 指定獨立的 `env.json`
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        # 測試執行完畢後刪除 `env.json`（避免污染環境）
        os.remove(env_file)

        self.executed_tests.append(self.module_name + key)

        # 失敗處理邏輯
        if key.startswith('api_test') and result.returncode != 0:
            failed_api_tests.append(self.module_name + "_" + key)
            for integration_test_name in self.urls:
                if integration_test_name.startswith('integration_test') and integration_test_name not in self.executed_tests:
                    unexecuted_integration_tests.append(self.module_name + "_" + integration_test_name)
            print(f"Newman命令執行失敗: {' '.join(command)}")
            print(f"返回碼: {result.returncode}")
            print(f"標準輸出: {result.stdout}")
            print(f"標準錯誤: {result.stderr}")
            raise ValueError(f"API 測試失敗: {key}\n\n")

        if key.startswith('integration_test') and result.returncode != 0:
            failed_integration_tests.append(self.module_name + "_" + key)

    def run_postman_test(self, max_workers=4, delay=3000):
        """使用 ThreadPoolExecutor 來併發執行多個測試"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.run_single_test, key, value, delay): key for key, value in self.urls.items()}

            for future in as_completed(futures):
                key = futures[future]
                try:
                    future.result()  # 這裡會抓取執行的 Exception
                except Exception as e:
                    print(f"測試 {key} 失敗: {e}")


# 在起始階段創建/清空失敗測試記錄文件
# (這樣寫法文件只會做一次的開啟和關閉，不會一直開啟關閉，迴圈內都會用相同的開啟和關閉)
def write_failed_tests_to_file():
    with open("failed_tests.txt", 'w') as failed_tests_file:
        if failed_api_tests:
            failed_tests_file.write("Failed API tests:\n\n")
            for test in failed_api_tests:
                failed_tests_file.write(test + "\n\n")
        if unexecuted_integration_tests:
            failed_tests_file.write("\nUnexecuted Integration tests:\n\n")
            for test in unexecuted_integration_tests:
                failed_tests_file.write(test + "\n\n")
        if failed_integration_tests:
            failed_tests_file.write("\nFailed Integration tests:\n\n")
            for test in failed_integration_tests:
                failed_tests_file.write(test + "\n\n")

def convert_json_to_word():
    for module_name, value in MODULE.items():
        for test_name, sub_value in value.items():
            json_report_path = f"json/report_{module_name}_{test_name}.json"
            if os.path.exists(json_report_path):
                with open(json_report_path, "r", encoding="utf-8") as f:
                    report_data = json.load(f)                    # 編輯/提取 JSON 資料
                WordConverter(module_name, test_name, report_data).create_word_report()

if __name__ == "__main__":
    try:
        # 記錄 API 測試和 Integration 測試的失敗測試名稱
        # python 的list是mutable(可變類型)，所以可以在函數內部與類別都可以直接修改全域變數
        failed_api_tests = []
        unexecuted_integration_tests = []
        failed_integration_tests = []

        max_workers = 4

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(CT(key, value).run_postman_test, max_workers): key
                for key, value in MODULE.items()
            }

            for future in as_completed(futures):
                key = futures[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"測試 {key} 失敗: {e}")

        # 單獨執行不併發的測試
        for module_name, value in MODULE_NON_CONCURRENT.items():
            CT(module_name, value).run_postman_test()

        # 將失敗測試記錄寫入文件
        write_failed_tests_to_file()
        convert_json_to_word()
    except Exception as e:
        import traceback
        print(f"Exception: {e}")
        print("詳細錯誤追蹤:")
        traceback.print_exc()