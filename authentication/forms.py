from .admin import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser,Shipper
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField


class MerchantRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('company_name', 'company_reg', 'first_name', 'last_name', 'email', 'address', 'state', 'telephone', 'bio',)


class MerchantEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('company_name', 'first_name', 'last_name', 'email', 'address', 'state', 'telephone', 'bio', 'password')


class ShopperRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone')


class ShopperEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone')


class ShipperRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'state', 'telephone', 'bio', )


class ShipperEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('company_name', 'first_name', 'last_name', 'email', 'address', 'state', 'telephone',)


location_options = [('Lagos', 'Lagos'), ('Abuja', 'Abuja'), ('Port Harcourt', 'Port Harcourt'), ('South-South',
                    'South-South'), ('South-East', 'South-East'), ('South-West', 'South-West'), ('North-East',
                    'North-East'), ('North-Central', 'North-Central'), ('North-West', 'North-West')]
unit_options = {('kilogram', 'Kilogram'), ('Grams', 'Grams')}
transport_type = [('Bike', 'Bike'), ('MiniBus', 'MiniBus')]


class ShipperForm(forms.ModelForm):

    class Meta:
        model = Shipper
        fields = ('vehicle_type', 'registration_name', 'registration_number', 'license_number', 'engine_number', 'brand',
                  'year_of_purchase', 'region', 'extra_info', )
