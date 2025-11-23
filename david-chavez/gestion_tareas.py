# gestion_tareas.py
tareas = []

def agregar_tarea():
    tarea = input("📝 Nueva tarea: ")
    tareas.append({"tarea": tarea, "completada": False})
    print("✅ Tarea agregada!")

def ver_tareas():
    if not tareas:
        print("📭 No hay tareas pendientes")
        return
    
    print("\n📋 LISTA DE TAREAS:")
    for i, tarea in enumerate(tareas, 1):
        estado = "✓" if tarea["completada"] else "✗"
        print(f"{i}. [{estado}] {tarea['tarea']}")

def marcar_completada():
    ver_tareas()
    if tareas:
        try:
            numero = int(input("\nNúmero de tarea a completar: ")) - 1
            if 0 <= numero < len(tareas):
                tareas[numero]["completada"] = True
                print("🎉 Tarea marcada como completada!")
            else:
                print("❌ Número inválido")
        except ValueError:
            print("❌ Ingresa un número válido")

def eliminar_tarea():
    ver_tareas()
    if tareas:
        try:
            numero = int(input("\nNúmero de tarea a eliminar: ")) - 1
            if 0 <= numero < len(tareas):
                tarea_eliminada = tareas.pop(numero)
                print(f"🗑️ Tarea eliminada: {tarea_eliminada['tarea']}")
            else:
                print("❌ Número inválido")
        except ValueError:
            print("❌ Ingresa un número válido")

def menu():
    while True:
        print("\n" + "="*30)
        print("🎯 GESTOR DE TAREAS")
        print("="*30)
        print("1. 📝 Agregar tarea")
        print("2. 👀 Ver tareas")
        print("3. ✅ Marcar tarea como completada")
        print("4. 🗑️ Eliminar tarea")
        print("5. 🚪 Salir")
        
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()