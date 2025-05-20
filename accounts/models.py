from django.db import models 
from django.contrib.auth.models import ( 
    AbstractUser,
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
) 

class UserManager(BaseUserManager): 
    def create_user(self, username, email, password=None): 
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email), 
            username = username,
            password = password
        )
        
        user.is_admin = True 
        user.is_active = True
        user.is_staff = True 
        user.is_superadmin = True 
        user.save(using=self._db) 
        return user  

class CustomUser(AbstractUser, PermissionsMixin): 
    email = models.EmailField(max_length=100, unique=True)  
    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=False)  
    is_superadmin = models.BooleanField(default=False)  

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()

    def __str__(self):
        return self.email 
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True