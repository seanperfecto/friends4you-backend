from django.utils.deprecation import MiddlewareMixin

class DisableCsrfCheck(MiddlewareMixin):

   def process_request(self, req):
        attr = '_dont_enforce_csrf_checks'
        setattr(req, attr, True)
