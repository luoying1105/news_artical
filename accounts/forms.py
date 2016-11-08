from django import forms
#用于的用户登录的表单 由于关联默认USER 不另外设用户类别
"""
echo "# news_artical" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/luoying1105/news_artical.git
git push -u origin master
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/luoying1105/newsartical.git
git push -u origin master
 accounts/
        artical/
        db.sqlite3
        image/
        manage.py
        news_artical/
        static/
        templates/

"""
class LoginForm(forms.Form):
 username = forms.CharField()
 password = forms.CharField(widget=forms.PasswordInput)