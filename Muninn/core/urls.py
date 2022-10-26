"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^useraccount/$', views.UserAccount_List),
    path(r'^useraccount/([0-9]*)$', views.UserAccount_Detail),
    path(r'^userconfig/$', views.UserConfig_List),
    path(r'^userconfig/([0-9]*)$', views.UserConfig_Detail),
    path(r'^molecule/$', views.Molecule_List),
    path(r'^molecule/([0-9]*)$', views.Molecule_Detail),
    path(r'^location/$', views.Location_List),
    path(r'^location/([0-9]*)$', views.Location_Detail),
    path(r'^row/$', views.Row_List),
    path(r'^row/([0-9]*)$', views.Row_Detail),
    path(r'^rack/$', views.Rack_List),
    path(r'^rack/([0-9]*)$', views.Rack_Detail),
    path(r'^atom/$', views.Atom_List),
    path(r'^atom/([0-9]*)$', views.Atom_Detail),
    path(r'^attribute/$', views.Attribute_List),
    path(r'^attribute/([0-9]*)$', views.Attribute_Detail),
    path(r'^chapter/$', views.Chapter_List),
    path(r'^chapter/([0-9]*)$', views.Chapter_Detail),
    path(r'^dictionary/$', views.Dictionary_List),
    path(r'^dictionary/([0-9]*)$', views.Dictionary_Detail),
    path(r'^objecttype/$', views.ObjectType_List),
    path(r'^objecttype/([0-9]*)$', views.ObjectType_Detail),
    path(r'^object/$', views.Object_List),
    path(r'^object/([0-9]*)$', views.Object_Detail),
    path(r'^attributemap/$', views.AttributeMap_List),
    path(r'^attributemap/([0-9]*)$', views.AttributeMap_Detail),
    path(r'^attributevaluestring/$', views.AttributeValueString_List),
    path(r'^attributevaluestrin/([0-9]*)$', views.AttributeValueStrin_Detail),
    path(r'^attributevalueint/$', views.AttributeValueInt_List),
    path(r'^attributevalueint/([0-9]*)$', views.AttributeValueInt_Detail),
    path(r'^attributevaluefloat/$', views.AttributeValueFloat_List),
    path(r'^attributevaluefloat/([0-9]*)$', views.AttributeValueFloat_Detail),
    path(r'^attributevaluedict/$', views.AttributeValueDict_List),
    path(r'^attributevaluedict/([0-9]*)$', views.AttributeValueDict_Detail),
    path(r'^attributevaluedate/$', views.AttributeValueDate_List),
    path(r'^attributevaluedate/([0-9]*)$', views.AttributeValueDate_Detail),
    path(r'^ipv4address/$', views.IPv4Address_List),
    path(r'^ipv4address/([0-9]*)$', views.IPv4Address_Detail),
    path(r'^ipv4vs/$', views.IPv4VS_List),
    path(r'^ipv4vs/([0-9]*)$', views.IPv4VS_Detail),
    path(r'^ipv4allocation/$', views.IPv4Allocation_List),
    path(r'^ipv4allocation/([0-9]*)$', views.IPv4Allocation_Detail),
    path(r'^ipv4rspool/$', views.IPv4RSPool_List),
    path(r'^ipv4rspool/([0-9]*)$', views.IPv4RSPool_Detail),
    path(r'^ipv4rs/$', views.IPv4RS_List),
    path(r'^ipv4rs/([0-9]*)$', views.IPv4RS_Detail),
    path(r'^ipv4lb/$', views.IPv4LB_List),
    path(r'^ipv4lb/([0-9]*)$', views.IPv4LB_Detail),
    path(r'^ipv4log/$', views.IPv4Log_List),
    path(r'^ipv4log/([0-9]*)$', views.IPv4Log_Detail),
    path(r'^ipv4nat/$', views.IPv4NAT_List),
    path(r'^ipv4nat/([0-9]*)$', views.IPv4NAT_Detail),
    path(r'^ipv4network/$', views.IPv4Network_List),
    path(r'^ipv4network/([0-9]*)$', views.IPv4Network_Detail),
    path(r'^ipv6address/$', views.IPv6Address_List),
    path(r'^ipv6address/([0-9]*)$', views.IPv6Address_Detail),
    path(r'^ipv6allocation/$', views.IPv6Allocation_List),
    path(r'^ipv6allocation/([0-9]*)$', views.IPv6Allocation_Detail),
    path(r'^ipv6log/$', views.IPv6Log_List),
    path(r'^ipv6log/([0-9]*)$', views.IPv6Log_Detail),
    path(r'^ipv6network/$', views.IPv6Network_List),
    path(r'^ipv6network/([0-9]*)$', views.IPv6Network_Detail),
    path(r'^config/$', views.Config_List),
    path(r'^config/([0-9]*)$', views.Config_Detail),
    path(r'^file/$', views.File_List),
    path(r'^file/([0-9]*)$', views.File_Detail),
    path(r'^filelinkipv4network/$', views.FileLinkIPv4Network_List),
    path(r'^filelinkipv4network/([0-9]*)$', views.FileLinkIPv4Network_Detail),
    path(r'^filelinkipv4rspool/$', views.FileLinkIPv4RSPool_List),
    path(r'^filelinkipv4rspool/([0-9]*)$', views.FileLinkIPv4RSPool_Detail),
    path(r'^filelinkipv4vs/$', views.FileLinkIPv4VS_List),
    path(r'^filelinkipv4vs/([0-9]*)$', views.FileLinkIPv4VS_Detail),
    path(r'^filelinkipv6network/$', views.FileLinkIPv6Network_List),
    path(r'^filelinkipv6network/([0-9]*)$', views.FileLinkIPv6Network_Detail),
    path(r'^filelinklocation/$', views.FileLinkLocation_List),
    path(r'^filelinklocation/([0-9]*)$', views.FileLinkLocation_Detail),
    path(r'^filelinkobject/$', views.FileLinkObject_List),
    path(r'^filelinkobject/([0-9]*)$', views.FileLinkObject_Detail),
    path(r'^filelinkrack/$', views.FileLinkRack_List),
    path(r'^filelinkrack/([0-9]*)$', views.FileLinkRack_Detail),
    path(r'^filelinkrow/$', views.FileLinkRow_List),
    path(r'^filelinkrow/([0-9]*)$', views.FileLinkRow_Detail),
    path(r'^filelinkuser/$', views.FileLinkUser_List),
    path(r'^filelinkuser/([0-9]*)$', views.FileLinkUser_Detail),
    path(r'^mountoperation/$', views.MountOperation_List),
    path(r'^mountoperation/([0-9]*)$', views.MountOperation_Detail),
    path(r'^objecthistory/$', views.ObjectHistory_List),
    path(r'^objecthistory/([0-9]*)$', views.ObjectHistory_Detail),
    path(r'^objectlog/$', views.ObjectLog_List),
    path(r'^objectlog/([0-9]*)$', views.ObjectLog_Detail),
    path(r'^patchcableconnector/$', views.PatchCableConnector_List),
    path(r'^patchcableconnector/([0-9]*)$', views.PatchCableConnector_Detail),
    path(r'^patchcabletype/$', views.PatchCableType_List),
    path(r'^patchcabletype/([0-9]*)$', views.PatchCableType_Detail),
    path(r'^patchcableconnectorcompat/$', views.PatchCableConnectorCompat_List),
    path(r'^patchcableconnector_detailcompat/([0-9]*)$', views.PatchCableConnector_DetailCompat),
    path(r'^patchcableheap/$', views.PatchCableHeap_List),
    path(r'^patchcableheap/([0-9]*)$', views.PatchCableHeap_Detail),
    path(r'^patchcableheaplog/$', views.PatchCableHeapLog_List),
    path(r'^patchcableheaplog/([0-9]*)$', views.PatchCableHeapLog_Detail),
    path(r'^plugin/$', views.Plugin_List),
    path(r'^plugin/([0-9]*)$', views.Plugin_Detail),
    path(r'^portinnerinterface/$', views.PortInnerInterface_List),
    path(r'^portinnerinterface/([0-9]*)$', views.PortInnerInterface_Detail),
    path(r'^portouterinterface/$', views.PortOuterInterface_List),
    path(r'^portouterinterface/([0-9]*)$', views.PortOuterInterface_Detail),
    path(r'^patchcableoifcompat/$', views.PatchCableOIFCompat_List),
    path(r'^patchcableoifcompat/([0-9]*)$', views.PatchCableOIFCompat_Detail),
    path(r'^port/$', views.Port_List),
    path(r'^port/([0-9]*)$', views.Port_Detail),
    path(r'^vlandomain/$', views.VLANDomain_List),
    path(r'^vlandomain/([0-9]*)$', views.VLANDomain_Detail),
    path(r'^vlandescription/$', views.VLANDescription_List),
    path(r'^vlandescription/([0-9]*)$', views.VLANDescription_Detail),
    path(r'^vlanipv4/$', views.VLANIPv4_List),
    path(r'^vlanipv4/([0-9]*)$', views.VLANIPv4_Detail),
    path(r'^vlanipv6/$', views.VLANIPv6_List),
    path(r'^vlanipv6/([0-9]*)$', views.VLANIPv6_Detail),
    path(r'^portallowedvlan/$', views.PortAllowedVLAN_List),
    path(r'^portallowedvlan/([0-9]*)$', views.PortAllowedVLAN_Detail),
    path(r'^portcompat/$', views.PortCompat_List),
    path(r'^portcompat/([0-9]*)$', views.PortCompat_Detail),
    path(r'^portinterfacecompat/$', views.PortInterfaceCompat_List),
    path(r'^portinterfacecompat/([0-9]*)$', views.PortInterfaceCompat_Detail),
    path(r'^portlog/$', views.PortLog_List),
    path(r'^portlog/([0-9]*)$', views.PortLog_Detail),
    path(r'^portvlanmode/$', views.PortVLANMode_List),
    path(r'^portvlanmode/([0-9]*)$', views.PortVLANMode_Detail),
    path(r'^rackobject/$', views.RackObject_List),
    path(r'^rackobject/([0-9]*)$', views.RackObject_Detail),
    path(r'^rackspace/$', views.RackSpace_List),
    path(r'^rackspace/([0-9]*)$', views.RackSpace_Detail),
    path(r'^rackthumbnail/$', views.RackThumbnail_List),
    path(r'^rackthumbnail/([0-9]*)$', views.RackThumbnail_Detail),
    path(r'^script/$', views.Script_List),
    path(r'^script/([0-9]*)$', views.Script_Detail),
    path(r'^tag/$', views.Tag_List),
    path(r'^tag/([0-9]*)$', views.Tag_Detail),
    path(r'^tagfile/$', views.TagFile_List),
    path(r'^tagfile/([0-9]*)$', views.TagFile_Detail),
    path(r'^tagipv4network/$', views.TagIPv4Network_List),
    path(r'^tagipv4network/([0-9]*)$', views.TagIPv4Network_Detail),
    path(r'^tagipv4rspool/$', views.TagIPv4RSPool_List),
    path(r'^tagipv4rspool/([0-9]*)$', views.TagIPv4RSPool_Detail),
    path(r'^tagipv4vs/$', views.TagIPv4VS_List),
    path(r'^tagipv4vs/([0-9]*)$', views.TagIPv4VS_Detail),
    path(r'^tagipv6network/$', views.TagIPv6Network_List),
    path(r'^tagipv6network/([0-9]*)$', views.TagIPv6Network_Detail),
    path(r'^taglocation/$', views.TagLocation_List),
    path(r'^taglocation/([0-9]*)$', views.TagLocation_Detail),
    path(r'^tagobject/$', views.TagObject_List),
    path(r'^tagobject/([0-9]*)$', views.TagObject_Detail),
    path(r'^tagrack/$', views.TagRack_List),
    path(r'^tagrack/([0-9]*)$', views.TagRack_Detail),
    path(r'^vlanstrule/$', views.VLANSTRule_List),
    path(r'^vlanstrule/([0-9]*)$', views.VLANSTRule_Detail),
    path(r'^vlanswitchtemplate/$', views.VLANSwitchTemplate_List),
    path(r'^vlanswitchtemplate/([0-9]*)$', views.VLANSwitchTemplate_Detail),
    path(r'^vlanswitch/$', views.VLANSwitch_List),
    path(r'^vlanswitch/([0-9]*)$', views.VLANSwitch_Detail),
    path(r'^vlanvalidid/$', views.VLANValidID_List),
    path(r'^vlanvalidid/([0-9]*)$', views.VLANValidID_Detail),
    path(r'^vs/$', views.VS_List),
    path(r'^vs/([0-9]*)$', views.VS_Detail),
    path(r'^vsenabledips/$', views.VSEnabledIPs_List),
    path(r'^vsenabledips/([0-9]*)$', views.VSEnabledIPs_Detail),
    path(r'^vsenabledports/$', views.VSEnabledPorts_List),
    path(r'^vsenabledports/([0-9]*)$', views.VSEnabledPorts_Detail),
    path(r'^vsips/$', views.VSIPs_List),
    path(r'^vsips/([0-9]*)$', views.VSIPs_Detail),
    path(r'^vsports/$', views.VSPorts_List),
    path(r'^vsports/([0-9]*)$', views.VSPorts_Detail),
]
