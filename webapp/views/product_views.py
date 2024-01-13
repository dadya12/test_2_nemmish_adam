from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm, ProductUserForm

class ProductListView(ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'
    paginate_by = 3

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['review'] = product.review_set.all()
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create_products.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:home')

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update_products.html'
    form_class = ProductForm
    context_object_name = 'products'
    permission_required = 'webapp.change_product'

    def has_permission(self):
        project = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.users.all() or self.request.user == self.get_object().users

    def get_success_url(self):
        return reverse('webapp:detail_product', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete_products.html'
    success_url = reverse_lazy('webapp:home')

class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUserForm
    template_name = 'update_user.html'
    context_object_name = 'project'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:detail_product', kwargs={'pk': self.object.pk})