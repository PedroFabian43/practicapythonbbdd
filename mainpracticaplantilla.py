from services import servicepractica as serv

print("-----Base de Datos de la Plantilla-----")
service = serv.ServicePlantilla()
lista = service.getPlantilla()
for empleado in lista:
    print(f"IdHos: {empleado.idHospital} \nSala: {empleado.idSala} \nNum.Empleado: {empleado.idEmpleado} \nNombre: {empleado.apellido} \nFunción: {empleado.funcion} \nTurno: {empleado.turno} \nSalario: {empleado.salario}")
    print("----------------------------------")
print("Fin de Programa")

