from guiaofertas.apps.accounts.views.Login import Login
from guiaofertas.apps.accounts.views.Logout import Logout

login = Login.as_view()
logout = Logout.as_view()