from helusers.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return ' - '.join([super().__str__(), self.get_display_name(), self.email])

    def get_display_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name).strip()

    def get_default_organization(self):
        return self.admin_organizations.order_by('created_at').first()
