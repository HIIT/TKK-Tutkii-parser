import xml.dom.minidom
import xpath
import copy

staff = {}

def _fix_name( name ):
    name = name.replace('\n', '')
    name = name.split('\t')
    name = name[1] + ', ' + name[0]
    name = unicode( name )
    print name
    return name

def init():
   data = open('./staff.txt' , 'r').readlines()
   data = map( _fix_name , data )
   for name in data:
       staff[name] = 0
   _staff = copy.deepcopy( staff )
   for member in staff:
       staff[member] = copy.deepcopy( _staff )

init()

xml = xml.dom.minidom.parse( './data.xml' )
list = xpath.find( '//ci', xml )

data = []

print '******'

for item in list:
   print item.firstChild.nodeValue
   line = item.firstChild.nodeValue.split(';')
   data.append( map( lambda x : unicode( x.strip() ) , line ) )

staff_list = staff.keys()

for item in data:
     print item
     if len( item ) > 1:
         # check against other staff members
         staff_count = 0
         staff_members = []
         for author in item:
             staff_count += staff_list.count( author )
             if staff_list.count( author ) > 0:
                  staff_members.append( author )
         if staff_count > 1:
            for member1 in staff_members:
                 for member2 in staff_members:
                     staff[member1][member2] += 1

print '--'

for q in sorted( staff_list ):
    print q.replace(',','') + ',' + ','.join( map( lambda x: str( staff[q][x] ) , sorted( staff[q].keys() ) ) )
