# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask.views import View

from flask import redirect, request, render_template


class FormView(View):
    methods = ['GET', 'POST']

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def redirect(self):
        return redirect(self.success_url)

    def dispatch_request(self, key_name=None):
        form = self.get_form(key_name=key_name)
        if request.method == 'POST':
            return self.form_handler(form=form, key_name=key_name)
        else:
            context = {'form': form, 'title': self.get_title()}
            return self.render_template(context)
