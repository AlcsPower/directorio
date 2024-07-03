import csv
import ldap3

# Configuración de conexión a Active Directory
server = 'ldap://172.1.1.1'
base_dn = 'dc=++,dc=++,dc=ni'
user = 'CN=,DC=gob,DC=ni'  # Nombre de usuario simple
password = 'pass'

# Atributos a recuperar
attributes = ['displayName', 'telephoneNumber', 'physicalDeliveryOfficeName']

# Conexión a Active Directory
conn = ldap3.Connection(server, user, password, auto_bind=True)

# Búsqueda de usuarios
conn.search(base_dn, '(objectClass=user)', attributes=attributes)

# Lista para almacenar los datos de los usuarios
usuarios = []

# Recolección de los datos de los usuarios
for entry in conn.entries:
    try:
        username = entry['displayName'][0]
    except IndexError:
        username = 'N/A'
    
    try:
        phone = entry['telephoneNumber'][0]
    except IndexError:
        phone = ''
    
    try:
        office = entry['physicalDeliveryOfficeName'][0]
    except IndexError:
        office = 'N/A'
    
    if phone:  # Guardar solo si el teléfono no está vacío
        usuarios.append((username, phone, office))

# Ordenar los usuarios alfabéticamente por el nombre
usuarios.sort()

# Creación del archivo CSV
with open('lista.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(['Nombre', 'Teléfono', 'Oficina'])

    # Escritura de los usuarios en el archivo CSV
    for usuario in usuarios:
        writer.writerow(usuario)

# Cierre de la conexión
conn.unbind()

print('Archivo CSV creado correctamente.')
