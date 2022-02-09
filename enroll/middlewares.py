# from django.shortcuts import HttpResponse
# # --------------------------------------Function Based MiddleWare---------------------------------

# # def my_middleware(get_response):
# #     print("one time intializaion")
# #     def my_function(request):
# #         print("this is before view")
# #         response = get_response(request)
# #         print("this is after view")
# #         return response
# #     return my_function


# # -------------------------------------------Class Based MiddleWare-----------------------------------

# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("one time initilization")
#     def __call__(self, request):
#         print("this is before view")
#         response = self.get_response(request)
#         print("this is after view")
#         return response
# # ------------------------------------------------Hooks MiddleWare----------------------------------------------------

# class MyProcessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#     def process_view(request,*args, **kwargs): # ya function name hmasha same e raha ga
#         print("this is process view --before view")
#         return None



# class MyExceptionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#     def process_exception(self, request, exception): # ya function name hmasha same e raha ga
#         print("Exception occured")
#         msg = exception
#         return HttpResponse(msg)


