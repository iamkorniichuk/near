class BasePopulateDataMixin:
    def update_request(self, request, *args, **kwargs):
        if hasattr(request.data, "_mutable") and request.data._mutable is False:
            request.data._mutable = True
        request.data.update(self.get_populated_data(*args, **kwargs))
        return request

    def get_populated_data(self, *args, **kwargs):
        raise NotImplementedError()


class PopulateCreateDataMixin(BasePopulateDataMixin):
    """
    Populate request's data on model create.

    Override `.get_populated_data()` to provide updated data.
    """

    def create(self, request, *args, **kwargs):
        request = self.update_request(request, *args, **kwargs)
        return super().create(request, *args, **kwargs)


class PopulateUpdateDataMixin(BasePopulateDataMixin):
    """
    Populate request's data on model update.

    Override `.get_populated_data()` to provide updated data.
    """

    def update(self, request, *args, **kwargs):
        request = self.update_request(request, *args, **kwargs)
        return super().update(request, *args, **kwargs)


class PopulateDataMixin(PopulateCreateDataMixin, PopulateUpdateDataMixin):
    """
    Populate request's data on model create and update.

    Override `.get_populated_data()` to provide updated data.
    """

    pass
