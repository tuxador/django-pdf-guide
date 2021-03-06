from django.conf.urls import include, url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^$', views.BookIndexTemplateView.as_view(), name='book_index',),
    url(r'^books_plain_old_view$', views.books_plain_old_view, name='books_plain_old_view',),
    url(r'^books_plain_old_view_content_disp$', views.books_plain_old_view_content_disp, name='books_plain_old_view_content_disp',),
    url(r'^book_pdf_detail_view/(?P<pk>[0-9]+)/$', views.BookPdfDetailView.as_view(), name='book_pdf_detail_view',),
    url(r'^book_pdf_list_view$', views.BookPdfListView.as_view(), name='book_pdf_list_view',),
    url(r'^book_list_ex$', views.BookExPdfListView.as_view(), name='book_list_ex',),
    url(r'^cover_book_list$', views.CoverBookPdfListView.as_view(), name='cover_book_list',),
    url(r'^book_pdf_card_detail/(?P<pk>[0-9]+)/$', views.BookCardPdfListView.as_view(), name='book_pdf_card_detail',),
]
