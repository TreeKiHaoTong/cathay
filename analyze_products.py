#!/usr/bin/env python3
import json
from collections import defaultdict
from typing import Dict, List, Tuple

def analyze_products_categories_and_prices(filename: str = "products.json") -> None:
    """
    Analyze products to find categories and their price ranges
    
    Args:
        filename: Path to the products JSON file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            products = json.load(f)
        
        print(f"總共載入 {len(products)} 個產品\n")
        
        # Dictionary to store category info and prices
        category_data = defaultdict(list)
        
        # Process each product
        for product in products:
            category_name = product.get('category', {}).get('name', 'Unknown')
            price = float(product.get('price', 0))
            
            category_data[category_name].append({
                'name': product.get('name'),
                'price': price
            })
        
        # Calculate statistics for each category
        print("=== 產品分類與價格範圍分析 ===\n")
        print(f"總共有 {len(category_data)} 個分類:\n")
        
        total_min_price = float('inf')
        total_max_price = float('-inf')
        
        for category, products_in_category in sorted(category_data.items()):
            prices = [p['price'] for p in products_in_category]
            min_price = min(prices)
            max_price = max(prices)
            avg_price = sum(prices) / len(prices)
            
            total_min_price = min(total_min_price, min_price)
            total_max_price = max(total_max_price, max_price)
            
            print(f"📂 {category}")
            print(f"   • 產品數量: {len(products_in_category)} 個")
            print(f"   • 價格範圍: ${min_price:.2f} - ${max_price:.2f}")
            print(f"   • 平均價格: ${avg_price:.2f}")
            print(f"   • 產品列表: {', '.join([p['name'] for p in products_in_category])}")
            print()
        
        print("=== 整體統計 ===")
        print(f"• 總分類數: {len(category_data)} 個")
        print(f"• 總產品數: {len(products)} 個") 
        print(f"• 整體價格範圍: ${total_min_price:.2f} - ${total_max_price:.2f}")
        
        # Show category distribution
        print(f"\n=== 分類產品數量分佈 ===")
        for category, products_in_category in sorted(category_data.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"• {category}: {len(products_in_category)} 個產品")
            
    except FileNotFoundError:
        print(f"找不到檔案: {filename}")
    except json.JSONDecodeError:
        print("JSON 格式錯誤")
    except Exception as e:
        print(f"分析時發生錯誤: {e}")

if __name__ == "__main__":
    analyze_products_categories_and_prices()