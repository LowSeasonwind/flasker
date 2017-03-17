#!/usr/bin/env python
# coding=utf-8

from flask import redirect, render_template, url_for
from app.user import user
from app.user.forms import MyForm

@user.route('/submit',methods = ['GET','POST'])
def submit():
    form  =MyForm()
    if form.validate_on_submit():
        return redirect('/asset/')
    return render_template('/user/index.html',form=form)
    
