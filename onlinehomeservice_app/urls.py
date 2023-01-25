from django.urls import path

from onlinehomeservice_app import views

urlpatterns=[
    path("",views.index,name="index"),
    path("index1",views.index1,name="index1"),
    path("loginpage",views.loginpage,name="loginpage"),




    path("base", views.adminbase, name="base"),
    path("feedbacks", views.feedbacks, name="feedbacks"),
    path("reply_feedback/<int:id>/", views.reply_feedback, name="reply_feedback"),
    path("view_schedule", views.view_schedule, name="view_schedule"),
    path("work_add", views.work_add, name="work_add"),
    path("work_view", views.work_view, name="work_view"),
    path("delete_work_view/<int:id>/", views.delete_work_view, name="delete_work_view"),
    path("update_work_view/<int:id>/", views.update_work_view, name="update_work_view"),
    path("admin_view_appointment", views.admin_view_appointment, name="admin_view_appointment"),
    path("approve_appointment/<int:id>/", views.approve_appointment, name="approve_appointment"),
    path("reject_appointment/<int:id>/", views.reject_appointment, name="reject_appointment"),
    path("bill", views.bill, name="bill"),
    path("view_bill", views.view_bill, name="view_bill"),
    path("customers_data", views.customers_data, name="customers_data"),
    path("delete_it/<int:id>/", views.delete_it, name="delete_it"),
    path("workers_data", views.workers_data, name="workers_data"),
    path("delete/<int:id>/", views.delete, name="delete"),


    path("workers", views.workers, name="workers"),
    path("workerbase", views.workerbase, name="workerbase"),
    path("worker_registration", views.worker_registration, name="worker_registration"),
    path("Schedule", views.Schedule, name="Schedule"),
    path("worker_view_schedule", views.worker_view_schedule, name="worker_view_schedule"),
    path("worker_view_appointment", views.worker_view_appointment, name="worker_view_appointment"),
    path("worker_update/<int:id>/", views.worker_update, name="worker_update"),

    path("customers", views.customers, name="customers"),
    path("customer_registration", views.customer_registration, name="customer_registration"),
    path("customerbase", views.customerbase, name="customerbase"),
    path("update/<int:id>/", views.update, name="update"),
    path("feedback", views.feedback, name="feedback"),
    path("view", views.view, name="view"),
    path("deletefeedback/<int:id>/", views.deletefeedback, name="deletefeedback"),
    path("delete_schedule/<int:id>/", views.delete_schedule, name="delete_schedule"),
    path("customer_view_schedule", views.customer_view_schedule, name="customer_view_schedule"),
    path("customer_view_worker", views.customer_view_worker, name="customer_view_worker"),
    path("take_appointment/<int:id>/", views.take_appointment, name="take_appointment"),
    path("view_appointment", views.view_appointment, name="view_appointment"),
    path("customer_view_payment", views.customer_view_payment, name="customer_view_payment"),
    path("creditcard_pay_cus", views.creditcard_pay_cus, name="creditcard_pay_cus"),
    path("view_creditcard_details", views.view_creditcard_details, name="view_creditcard_details"),
    path("pay_bill/<int:id>/", views.pay_bill, name="pay_bill"),
    path("pay_in_direct/<int:id>/", views.pay_in_direct, name="pay_in_direct"),
    path("bill_history", views.bill_history, name="bill_history"),

]