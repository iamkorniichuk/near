class BasePopulateDataMixin:
    # TODO: Add docstrings
    def update_request(self, request):
        request.data._mutable = True
        request.data.update(self.get_populated_data())
        request.data._mutable = False
        return request

    def get_populated_data(self):
        raise NotImplementedError()


class PopulateCreateDataMixin(BasePopulateDataMixin):
    def create(self, request, *args, **kwargs):
        request = self.update_request(request)
        return super().create(request, *args, **kwargs)


class PopulateUpdateDataMixin(BasePopulateDataMixin):
    def update(self, request, *args, **kwargs):
        request = self.update_request(request)
        return super().update(request, *args, **kwargs)


class PopulateDataMixin(PopulateCreateDataMixin, PopulateUpdateDataMixin):
    pass
