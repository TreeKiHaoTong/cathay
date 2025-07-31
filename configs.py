PRODUCT = {
    'api_test' : 'api_test/product/cathay_product.postman_collection.json' 
}

CATEGORY = {
    'api_test' : 'api_test/category/cathay_category.postman_collection.json'
}

BRAND = {
    'api_test' : 'api_test/brand/cathay_brand.postman_collection.json'
}

# GRAPH = {
#     'api_test' : 'api_test/graph/CORE_graph.postman_collection.json'
# }

# ORGANIZATION = {
#     'api_test' : 'api_test/organization/CORE_organization.postman_collection.json'
# }

# USER_ADMIN = {
#     'api_test' : 'api_test/user/CORE_user(admin).postman_collection.json'
# }

# USER_MANAGER = {
#     'api_test' : 'api_test/user/CORE_user(manager).postman_collection.json'
# }

# USER_USER = {
#     'api_test' : 'api_test/user/CORE_user(user).postman_collection.json'
# }

# CASE = {
#     'api_test' : 'api_test/case/CORE_case.postman_collection.json'
# }

# TRACK = {
#     'api_test' : 'api_test/track/CORE_track.postman_collection.json'
# }

# CASE_DOC = {
#     'api_test' : 'api_test/case_doc/CORE_case-doc.postman_collection.json'
# }

# 併發執行的測試
MODULE = {'product': PRODUCT, 'category': CATEGORY, 'brand': BRAND}

# 不併發執行的測試，會在併發測試結束後，依序執行
# MODULE_NON_CONCURRENT = {'audit_log': AUDIT_LOG}

# MODULE_SCHEDULE = {'case_doc': CASE_DOC}