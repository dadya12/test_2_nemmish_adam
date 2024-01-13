from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from webapp.models import Review, Product
from django.shortcuts import render, reverse, get_object_or_404, redirect
from webapp.forms import ReviewForm


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/detail_review.html'

class ReviewCreateView(PermissionRequiredMixin, CreateView):
    form_class = ReviewForm
    template_name = 'review/create_review.html'
    permission_required = 'webapp.add_review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        context['product'] = product
        return context

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:detail_product', kwargs={'pk': self.kwargs['pk']})