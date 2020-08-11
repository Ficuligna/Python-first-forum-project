from django.contrib.auth.mixins import UserPassesTestMixin


class CreaSezioneMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff
