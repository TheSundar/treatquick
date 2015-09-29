from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from serializers import CustomUser, Group,Address
from rest_framework import viewsets
from rest_framework import status
from user_group.serializers import UserSerializer, GroupSerializer,AddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    print 'herer','----------------------'
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        location = request.data.pop('location')
        request.data.pop('groups')
        print type(location)
        address = AddressSerializer(data=location)
        # address.save()

        if address.is_valid(raise_exception=True):

            address.save()
            details = dict(request.data)

            user = CustomUser(location=Address.objects.get(id = address.data['id']),**details)
            user.save()
            details['id'] = user.id
            details['location'] = location


            return Response(details, status=status.HTTP_201_CREATED)
        else:
            print '_________'
        print request.data


    # def perform_create(self, serializer):
    #     print self.request.data,'****'
    #     serializer.save(owner=self.request.user)

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('-city')
    serializer_class = AddressSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer