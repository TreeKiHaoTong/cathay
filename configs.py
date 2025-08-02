PRODUCT = {
    'api_test' : 'api_test/product/cathay_products.postman_collection.json' 
}

CATEGORIES = {
    'api_test' : 'api_test/categories/cathay_categories.postman_collection.json'
}

BRAND = {
    'api_test' : 'api_test/brand/cathay_brands.postman_collection.json'
}

MESSAGE = {
    'api_test' : 'api_test/message/cathay_messages.postman_collection.json'
}

# 併發執行的測試
MODULE = {
    'product': PRODUCT,
    'categories': CATEGORIES,
    'brand': BRAND,
    'message': MESSAGE
}

# 不併發執行的測試，會在併發測試結束後，依序執行
MODULE_NON_CONCURRENT = {}