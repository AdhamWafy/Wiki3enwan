from django.forms import ModelForm
from .models import enwaan
from django.utils.text import slugify  # Import slugify function
from django.shortcuts import get_object_or_404
from anyascii import anyascii


class enwaanForm(ModelForm):
    class Meta:
        model = enwaan
        fields = ['الأسم_والمنطقة', 'العنوان', 'الرقم','الوصف','مقاطعة']
        # fields = '__all__'
        
    def save(self, commit=True): 
        instance = super().save(commit=False)
        
        if instance.الوصف == None:
            instance.الوصف = 'لا يوجد وصف'
        
        if instance.الرقم== None:
            instance.الرقم = 'لا يوجد رقم'
            
        if instance.مقاطعة == False:
            instance.text= 'لا'
            
        if instance.مقاطعة == True:
            instance.text= 'نعم'
        
        english = anyascii(instance.الأسم_والمنطقة)
        instance.slug = slugify(english,allow_unicode=True)
        if commit:
            instance.save()
        return instance
    
class EditForm(ModelForm):
    class Meta:
        model = enwaan
        fields = ['العنوان', 'الرقم','الوصف','مقاطعة']
        # fields = '__all__'
        
    def save(self, commit=True):
        instance = super().save(commit=False)  # Get the instance without saving

        # Retrieve the existing record based on the slug
        slug = self.instance.slug  # Access the slug from the current instance
        existing_record = get_object_or_404(enwaan, slug=slug)

        # Update the existing record's fields
        existing_record.العنوان = self.cleaned_data['العنوان']
        existing_record.الرقم = self.cleaned_data['الرقم']
        existing_record.الوصف = self.cleaned_data['الوصف']
        existing_record.مقاطعة = self.cleaned_data['مقاطعة']
        
        if self.cleaned_data['الوصف'] == None:
            existing_record.الوصف = 'لا يوجد وصف'
            
        if self.cleaned_data['الرقم']== None:
            existing_record.الرقم = 'لا يوجد رقم'
            
        if self.cleaned_data['مقاطعة']== False:
            existing_record.text = 'لا'
            
        if self.cleaned_data['مقاطعة']== True:
            existing_record.text = 'نعم'

        if commit:
            existing_record.save()
        return existing_record
    
