from odoo import http

class WorkWebCon(http.Controller):
    @http.route('/webwok/onwork', auth='public', website=True)
    def display_subject(self, **kwargs):

        sale_orders = http.request.env['sale.order'].search([])
        return http.request.render('works.webonwork',{
            'sale_orders': sale_orders,
        })
        # return 'Hello'


    @http.route("/webwork_des/<model('sale.order'):courses>", auth='public', website=True, type='http')
    def display_name(self, courses):

        template= 'works.webwork_discus'
        return http.request.render(template, {'courses': courses})
        # return f"Here is list = {courses.name}"

    #




