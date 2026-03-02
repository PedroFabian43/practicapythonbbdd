from services import servicepractica


print("-----Base de Datos de la Plantilla-----")
service = servicepractica.ServicePlantilla()
lista = service.getPlantilla()
for empleado in lista:
    print(f"IdHos: {empleado.idHospital} \nSala: {empleado.idSala} \nNum.Empleado: {empleado.idEmpleado} \nNombre: {empleado.apellido} \nFunción: {empleado.funcion} \nTurno: {empleado.turno} \nSalario: {empleado.salario}")
    print("----------------------------------")
print("Fin de Programa")

