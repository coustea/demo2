from rest_framework.pagination import PageNumberPagination
# 自定义分页器
class MyPageNumberPagination(PageNumberPagination):
    page_size = 5  # 每页显示的数据
    page_query_param = 'page' # 查询参数
    page_size_query_description = 'size'
    max_page_size = 5
    pass
