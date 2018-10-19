#_*_coding:utf-8_*_
__author__ = 'weihaoxuan'
from django.db import models
import django.utils.timezone as timezone
# from Integrated.user_models import UserProfile
# Create your models here.

class Asset(models.Model):
    asset_type_choices = (
        ('server', u'服务器'),
        ('Knifebox', u'刀箱'),
        ('switch', u'交换机'),
        ('router', u'路由器'),
        ('firewall', u'防火墙'),
        ('storage', u'存储设备'),
        ('NLB', u'NetScaler'),
        ('wireless', u'无线AP'),
        ('software', u'软件资产'),
        ('others', u'其它类'),
    )
    statuss = (
        ('start', u'在用'),
        ('Disable', u'停用未下架'),
        ('Disable_down', u'停用已下架'),
        ('maintain', u'维修'),
    )
    asset_type = models.CharField(choices=asset_type_choices,max_length=64, default='server')
    name = models.CharField(max_length=64)
    sn = models.CharField(u'资产SN号',max_length=128, unique=True)
    manufactory = models.ForeignKey('Manufactory',verbose_name=u'制造商',null=True, blank=True)
    management_ip = models.GenericIPAddressField(u'管理IP',blank=True,null=True)
    contract = models.ForeignKey('Contract', verbose_name=u'合同',null=True, blank=True)
    trade_date = models.DateField(u'购买时间',null=True, blank=True)
    expire_date = models.DateField(u'过保修期',null=True, blank=True)
    price = models.FloatField(u'价格',null=True, blank=True)
    disk_total = models.FloatField(u'硬盘总量(G)',null=True, blank=True)
    mem_total = models.FloatField(u'内存总量(G)',null=True, blank=True)
    business_unit = models.ForeignKey('BusinessUnit', verbose_name=u'所属业务线',null=True, blank=True)
    tags = models.ManyToManyField('Tag' ,blank=True)
    idc = models.ForeignKey('IDC', verbose_name=u'IDC机房',null=True, blank=True)
    cabinet = models.ForeignKey('Cabinet', verbose_name=u'所在机柜',null=True, blank=True)
    cabinet_begin = models.IntegerField(verbose_name=u'开始槽位',null=True, blank=True)
    cabinet_end = models.IntegerField(verbose_name=u'结束槽位',null=True, blank=True)
    status = models.CharField(choices=statuss,verbose_name=u'状态',max_length=64, default='start')
    memo = models.TextField(u'备注', null=True, blank=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, auto_now=True)
    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"
    def __unicode__(self):
        return 'id:%s name:%s'  %(self.id,self.name )


class Server(models.Model):
    asset = models.OneToOneField('Asset')
    created_by_choices = (
        ('auto','Auto'),
        ('manual','Manual'),
    )
    created_by = models.CharField(choices=created_by_choices,max_length=32,default='auto') #auto: auto created,   manual:created manually
    hosted_on = models.ForeignKey('self',related_name='hosted_on_server',blank=True,null=True) #for vitural server
    model = models.CharField(u'型号',max_length=128,null=True, blank=True )
    os_type  = models.CharField(u'操作系统类型',max_length=64, blank=True,null=True)
    os_distribution =models.CharField(u'发型版本',max_length=64, blank=True,null=True)
    os_release  = models.CharField(u'操作系统版本',max_length=64, blank=True,null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"

    def __unicode__(self):
        return '%s sn:%s' %(self.asset.name,self.asset.sn)


class NetworkDevice(models.Model):
    asset = models.OneToOneField('Asset')
    vlan_ip = models.GenericIPAddressField(u'VlanIP',blank=True,null=True)
    intranet_ip = models.GenericIPAddressField(u'内网IP',blank=True,null=True)
    sn = models.CharField(u'SN号',max_length=128,unique=True)
    #manufactory = models.CharField(verbose_name=u'制造商',max_length=128,null=True, blank=True)
    model = models.CharField(u'型号',max_length=128,null=True, blank=True )
    port_num = models.SmallIntegerField(u'端口个数',null=True, blank=True )
    device_detail = models.TextField(u'设置详细配置',null=True, blank=True )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = "网络设备"


class CPU(models.Model):

    asset = models.OneToOneField('Asset')
    cpu_model = models.CharField(u'CPU型号', max_length=128,blank=True)
    cpu_count = models.SmallIntegerField(u'物理cpu个数')
    cpu_core_count = models.SmallIntegerField(u'cpu核数')
    memo = models.TextField(u'备注', null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name = 'CPU部件'
        verbose_name_plural = "CPU部件"
    def __unicode__(self):
        return self.cpu_model

class RAM(models.Model):
    asset = models.ForeignKey('Asset')
    sn = models.CharField(u'SN号', max_length=128, blank=True,null=True)
    model =  models.CharField(u'内存型号', max_length=128)
    slot = models.CharField(u'插槽', max_length=64)
    capacity = models.IntegerField(u'内存大小(MB)')
    memo = models.CharField(u'备注',max_length=128, blank=True,null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)
    def __unicode__(self):
        return '%s:%s:%s' % (self.asset_id,self.slot,self.capacity)
    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = "RAM"
        unique_together = ("asset", "slot")
    auto_create_fields = ['sn','slot','model','capacity']

class Disk(models.Model):
    asset = models.ForeignKey('Asset')
    sn = models.CharField(u'SN号', max_length=128, blank=True,null=True)
    slot = models.CharField(u'插槽位',max_length=64)
    manufactory = models.CharField(u'制造商', max_length=64,blank=True,null=True)
    model = models.CharField(u'磁盘型号', max_length=128,blank=True,null=True)
    capacity = models.FloatField(u'磁盘容量GB')
    disk_iface_choice = (
        ('SATA', 'SATA'),
        ('SAS', 'SAS'),
        ('SCSI', 'SCSI'),
        ('SSD', 'SSD'),
    )

    iface_type = models.CharField(u'接口类型', max_length=64,choices=disk_iface_choice,default='SAS')
    memo = models.TextField(u'备注', blank=True,null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    auto_create_fields = ['sn','slot','manufactory','model','capacity','iface_type']
    class Meta:
        unique_together = ("asset", "slot")
        verbose_name = '硬盘'
        verbose_name_plural = "硬盘"
    def __unicode__(self):
        return '%s:slot:%s capacity:%s' % (self.asset_id,self.slot,self.capacity)


class NIC(models.Model):
    asset = models.ForeignKey('Asset')
    name = models.CharField(u'网卡名', max_length=64, blank=True,null=True)
    sn = models.CharField(u'SN号', max_length=128, blank=True,null=True)
    model =  models.CharField(u'网卡型号', max_length=128, blank=True,null=True)
    macaddress = models.CharField(u'MAC', max_length=64,unique=True)
    ipaddress = models.GenericIPAddressField(u'IP', blank=True,null=True)
    netmask = models.CharField(max_length=64,blank=True,null=True)
    bonding = models.CharField(max_length=64,blank=True,null=True)
    memo = models.CharField(u'备注',max_length=128, blank=True,null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return '%s:%s' % (self.asset_id,self.macaddress)
    class Meta:
        verbose_name = u'网卡'
        verbose_name_plural = u"网卡"
    auto_create_fields = ['name','sn','model','macaddress','ipaddress','netmask','bonding']

class RaidAdaptor(models.Model):
    asset = models.ForeignKey('Asset')
    sn = models.CharField(u'SN号', max_length=128, blank=True,null=True)
    slot = models.CharField(u'插口',max_length=64)
    model = models.CharField(u'型号', max_length=64,blank=True,null=True)
    memo = models.TextField(u'备注', blank=True,null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        unique_together = ("asset", "slot")

class Manufactory(models.Model):
    manufactory = models.CharField(u'厂商名称',max_length=64, unique=True)
    support_num = models.CharField(u'型号',max_length=30,blank=True)
    memo = models.CharField(u'服务器配置',max_length=128,blank=True)
    def __unicode__(self):
        return self.manufactory
    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = "厂商"

class Knifebox(models.Model):
    asset = models.ForeignKey('Asset')
    name = models.CharField(u'名称',max_length=64, unique=True)
    Intranet_ip = models.GenericIPAddressField(u'内网IP', blank=True, null=True)
    Outside_ip = models.GenericIPAddressField(u'外网IP', blank=True, null=True)
    memo = models.CharField(u'备注',max_length=64, null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '刀箱详情'
        verbose_name_plural = "刀箱详情"

class BusinessUnit(models.Model):
    parent_unit = models.ForeignKey('self',related_name='parent_level',blank=True,null=True)
    name = models.CharField(u'业务线',max_length=64, unique=True)

    #contact = models.ForeignKey('UserProfile',default=None)
    memo = models.CharField(u'备注',max_length=64, blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = "业务线"


class Contract(models.Model):
    sn = models.CharField(u'合同号', max_length=128,unique=True)
    name = models.CharField(u'合同名称', max_length=64 )
    memo = models.TextField(u'备注', blank=True,null=True)
    price = models.IntegerField(u'合同金额')
    detail = models.TextField(u'合同详细',blank=True,null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    license_num = models.IntegerField(u'license数量',blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date= models.DateField(auto_now=True)
    class Meta:
        verbose_name = '合同'
        verbose_name_plural = "合同"
    def __unicode__(self):
        return self.name

class IDC(models.Model):
    name = models.CharField(u'机房名称',max_length=64,unique=True)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '机房'
        verbose_name_plural = "机房"

class Cabinet(models.Model):
    name = models.CharField(u'机柜名称',max_length=64,unique=True)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '机柜表'
        verbose_name_plural = "机柜表"


class Tag(models.Model):
    name = models.CharField('Tag name',max_length=32,unique=True )
    # creater = models.ForeignKey('UserProfile')
    create_date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.name

class Notice(models.Model):
    name = models.CharField('通知内容', max_length=32)
    status = models.IntegerField('状态')
    create_date = models.DateTimeField(auto_now = True,blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '通知表'
        verbose_name_plural = "通知表"

#增加自用服务器表单
class RoomAsset(models.Model):
    asset_type_choices = (
        ('server', u'物理服务器'),
    )
    statuss = (
        ('start', u'在用'),
        ('Disable', u'停用未下架'),
        ('Disable_down', u'停用已下架'),
        ('maintain', u'维修'),
    )
    asset_type = models.CharField(choices=asset_type_choices,max_length=64, default='server')
    name = models.CharField(u'运维资产编号',max_length=64)
    Sn = models.CharField(u'资产SN号',max_length=128, unique=True)
    Brand = models.CharField(u'制造商品牌',max_length=128,null=True, blank=True)
    Model = models.CharField(u'型号',max_length=128,null=True, blank=True)
    ServerConfig = models.CharField(u'服务器配置',max_length=256,null=True, blank=True)
    Cabinet = models.CharField(u'机柜',max_length=128,null=True, blank=True)
    Slot = models.CharField(u'槽位',max_length=128,null=True, blank=True)
    ServiceModule = models.CharField(u'服务模块',max_length=128,null=True, blank=True)
    System = models.CharField(u'物理机系统',max_length=128,null=True, blank=True)
    RaidInfo = models.CharField(u'Raid卡信息',max_length=128,null=True, blank=True)
    MacInfo = models.CharField(u'MAC信息',max_length=128,null=True, blank=True)
    TorCabinet = models.CharField(u'TOR机柜',max_length=128,null=True, blank=True)
    ilo = models.GenericIPAddressField('ilo IP',max_length=128,null=True, blank=True)
    SubnetMask = models.CharField(u'子网掩码',max_length=64,null=True, blank=True)
    Gateway_ip = models.GenericIPAddressField(u'网关 IP',blank=True,null=True)
    Inband_ip = models.GenericIPAddressField(u'带内 IP',blank=True,null=True)
    Inband_SubnetMask = models.CharField(u'带内IP子网掩码',max_length=64,null=True, blank=True)
    Inband_Gateway_ip = models.GenericIPAddressField(u'带内网关 IP',blank=True,null=True)
    BGP_ip = models.GenericIPAddressField(u'BGP IP',blank=True,null=True)
    BGP_SubnetMask = models.CharField(u'BGP IP子网掩码',max_length=64,null=True, blank=True)
    BGP_Gateway_ip = models.GenericIPAddressField(u'BGP网关 IP',blank=True,null=True)
    nic1 = models.CharField(u'万兆网口1',max_length=32,null=True, blank=True)
    nic2 = models.CharField(u'万兆网口2',max_length=32,null=True, blank=True)
    nic3 = models.CharField(u'万兆网口3',max_length=32,null=True, blank=True)
    nic4 = models.CharField(u'万兆网口4',max_length=32,null=True, blank=True)
    nic5 = models.CharField(u'万兆网口5',max_length=32,null=True, blank=True)
    nic6 = models.CharField(u'万兆网口6',max_length=32,null=True, blank=True)
    Owner = models.ForeignKey('People', verbose_name=u'录入人员',null=True, blank=True)
    trade_date = models.DateField(u'购买时间',null=True, blank=True)
    expire_date = models.DateField(u'过保修期',null=True, blank=True)
    idc = models.ForeignKey('IDC', verbose_name=u'IDC机房',null=True, blank=True)
    status = models.CharField(choices=statuss,verbose_name=u'状态',max_length=64, default='start')
    memo = models.TextField(u'备注', null=True, blank=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, auto_now=True)
    class Meta:
        verbose_name = "新服务器表"
        verbose_name_plural = "新服务器表"
    def __unicode__(self):
        return 'id:%s name:%s'  %(self.id,self.name )

class People(models.Model):
    Name = models.CharField(u'姓名',max_length=64,unique=True)
    PhoneNumber = models.CharField(u'电话号码',max_length=30,blank=True,null=True)
    def __unicode__(self):
        return self.Name
    class Meta:
        verbose_name = '录入人员'
        verbose_name_plural = "录入人员信息"
