from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    # 업로드를 끝낸 후 이동할 페이지를 호출하기 위해 사용하는 메서드
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photo':photos})