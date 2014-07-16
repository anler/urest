# -*- coding: utf-8 -*-


def get_model(queryset, param="id"):
    def datasource(request):
        filters = {param: request.get_group(param)}
        return queryset.get(**filters)
    return datasource


def list_model(queryset):
    def datasource(request):
        return queryset.all()[request.pagination.start_index:request.pagination.page_size]
    return datasource
