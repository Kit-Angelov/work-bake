from django.core.mail import send_mail


def send_email(type, from_to, **kwargs):
    if type == 'call':
        send_mail('Звонок',
                  'Имя: {0}\nАдрес: {1}\nТелефон: {2}\nДата: {3}'.format(kwargs['name'],
                                                                                 kwargs['address'],
                                                                                 kwargs['phone'],
                                                                                 str(kwargs['order_date'])),
                  from_to[0],
                  [from_to[1]],
                  fail_silently=False,
                  )

    if type == 'order':
        elem_list = kwargs['elem_list']
        order = str()
        for attr in elem_list:
            order += '--------\nПродукт: {0}\nКод-во: {1} Упк.\nСумма: {2} Р\n-------'.format(str(attr[0]), str(attr[1]), str(attr[2]))
        send_mail('Заказ',
                  'Имя: {0}\nАдрес: {1}\nТелефон: {2}\nДата заказа: {3}\nСумма заказа: {4} Р.\n{5}'.format(
                      kwargs['name'],
                      kwargs['address'],
                      kwargs['phone'],
                      str(kwargs['order_date']),
                      str(kwargs['order_sum']),
                      order),
                  from_to[0],
                  [from_to[1]],
                  fail_silently=False,
                  )
