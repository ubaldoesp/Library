from rest_framework.permissions import BasePermission

class AllPermissions(BasePermission):
    
    def has_permission(self, request, view):
        print('has permission',view,request.method,view.action)
        if request.method == 'POST' and not request.user.is_staff:
            return False
        return True
    
    def has_object_permission(self, request, view, obj):
        print('has object_permission',view,obj)
        
        if request.method == 'GET':
            return True
        if request.user.is_authenticated and request.method in ['PATCH','PUT']:
            return True
        if request.method == 'DELETE' and request.user == obj.user:
            return True 
        return False