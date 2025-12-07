# ♻️ Ecomun - Sistema de Gestión de Reciclaje

<div align="center">

![Flutter](https://img.shields.io/badge/Flutter-3.9.2-02569B?logo=flutter)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?logo=firebase&logoColor=black)
![Dart](https://img.shields.io/badge/Dart-0175C2?logo=dart)
![License](https://img.shields.io/badge/License-MIT-green)

**Una aplicación móvil para facilitar el reciclaje y la gestión de residuos en tu comunidad**

[Características](#-características) • [Instalación](#-instalación) • [Uso](#-uso) • [Tecnologías](#-tecnologías)

</div>

---

## 📖 Descripción

**Ecomun** es una aplicación móvil desarrollada con Flutter que conecta a usuarios con servicios de recolección de materiales reciclables. La plataforma permite a los usuarios registrar solicitudes de recojo, aprender sobre materiales reciclables y hacer seguimiento de su impacto ambiental.

### 🎯 Objetivo

Promover prácticas de reciclaje sostenibles facilitando la gestión y recolección de materiales reciclables en comunidades urbanas, contribuyendo a la reducción de residuos y al cuidado del medio ambiente.

### ✨ Características Principales

- 🔐 **Autenticación de Usuarios**: Registro e inicio de sesión seguro con Firebase Authentication
- 📋 **Gestión de Solicitudes**: Crea y gestiona solicitudes de recojo de materiales reciclables
- ♻️ **Catálogo de Materiales**: Información detallada sobre tipos de materiales reciclables y consejos
- 📊 **Estadísticas Personales**: Visualiza tu impacto ambiental y cantidad reciclada
- 👤 **Perfil de Usuario**: Gestiona tu información personal y ubicación
- 🔔 **Actualizaciones en Tiempo Real**: Sincronización automática con Firebase Firestore
- 📱 **Diseño Responsivo**: Interfaz moderna y adaptable a diferentes dispositivos

---

## 🚀 Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- [Flutter SDK](https://flutter.dev/docs/get-started/install) (v3.9.2 o superior)
- [Dart SDK](https://dart.dev/get-dart) (incluido con Flutter)
- [Android Studio](https://developer.android.com/studio) o [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- Una cuenta de [Firebase](https://console.firebase.google.com/)

### 📦 Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/ecomun.git
cd ecomun/ecomun
```

### 🔧 Paso 2: Instalar Dependencias

```bash
flutter pub get
```

### 🔥 Paso 3: Configurar Firebase

#### 3.1 Crear Proyecto Firebase

1. Ve a [Firebase Console](https://console.firebase.google.com/)
2. Clic en **"Agregar proyecto"**
3. Nombre del proyecto: `Ecomun`
4. Sigue los pasos y crea el proyecto

#### 3.2 Configurar Firebase en la App

**Opción A: Usar FlutterFire CLI (Recomendado)**

```bash
# Instalar FlutterFire CLI
dart pub global activate flutterfire_cli

# Configurar Firebase
flutterfire configure
```

Selecciona tu proyecto `Ecomun` y las plataformas que desees (Android/iOS).

**Opción B: Manual**

Si ya tienes el archivo `firebase_options.dart`, asegúrate de que contenga tus credenciales correctas.

#### 3.3 Habilitar Servicios Firebase

**Authentication:**
1. Firebase Console → **Authentication** → **Get Started**
2. Pestaña **"Sign-in method"**
3. Habilita **"Email/Password"**
4. Guarda

**Firestore Database:**
1. Firebase Console → **Firestore Database** → **Create database**
2. Selecciona **"Start in test mode"**
3. Elige tu región preferida
4. Clic en **"Enable"**

#### 3.4 Configurar Reglas de Seguridad

En **Firestore Database** → **Rules**, pega el siguiente código:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // Reglas para usuarios
    match /users/{userId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && request.auth.uid == userId;
    }
    
    // Reglas para materiales
    match /materials/{materialId} {
      allow read: if true;
      allow write: if request.auth != null;
    }
    
    // Reglas para solicitudes
    match /requests/{requestId} {
      allow read: if request.auth != null && 
                     resource.data.userId == request.auth.uid;
      allow create: if request.auth != null && 
                       request.resource.data.userId == request.auth.uid;
      allow update, delete: if request.auth != null && 
                               resource.data.userId == request.auth.uid;
    }
  }
}
```

Clic en **"Publish"**

---

## ▶️ Ejecución

### Ejecutar en Modo Debug

```bash
flutter run
```

### Ejecutar en Dispositivo Específico

```bash
# Ver dispositivos disponibles
flutter devices

# Ejecutar en dispositivo específico
flutter run -d <device-id>
```

### Ejecutar en Modo Release (Producción)

```bash
flutter run --release
```

### Ejecutar en Emulador

**Android:**
```bash
# Iniciar emulador Android
emulator -avd <nombre_emulador>

# En otra terminal
flutter run
```

**iOS (Solo en macOS):**
```bash
open -a Simulator
flutter run
```

---

## 🎮 Uso

### Primera Ejecución

1. **Registro de Usuario**
   - Abre la aplicación
   - Clic en **"¿No tienes cuenta? Regístrate"**
   - Completa el formulario con:
     - Nombre completo
     - Correo electrónico
     - Contraseña (mínimo 6 caracteres)
     - Ubicación (opcional)
   - Clic en **"Registrarse"**

2. **Iniciar Sesión**
   - Ingresa tu correo y contraseña
   - Clic en **"Iniciar Sesión"**

3. **Explorar Materiales**
   - Desde el menú lateral → **"Materiales"**
   - Visualiza los tipos de materiales reciclables
   - Lee consejos sobre cómo reciclar correctamente

4. **Crear Solicitud de Recojo**
   - Desde la pantalla principal → **"Solicitar recojo"**
   - Selecciona el tipo de material
   - Ingresa la cantidad (kg)
   - Selecciona la fecha
   - Agrega observaciones (opcional)
   - Clic en **"Enviar solicitud"**

5. **Ver Estadísticas**
   - En la pantalla principal verás:
     - Total reciclado (kg)
     - Solicitudes completadas
   - Desde el menú → **"Perfil"** para más detalles

---

## 🛠️ Tecnologías

### Frontend

- **[Flutter](https://flutter.dev/)** - Framework de desarrollo multiplataforma
- **[Dart](https://dart.dev/)** - Lenguaje de programación
- **[Provider](https://pub.dev/packages/provider)** - Gestión de estado
- **[GoRouter](https://pub.dev/packages/go_router)** - Navegación y routing

### Backend

- **[Firebase Authentication](https://firebase.google.com/products/auth)** - Autenticación de usuarios
- **[Cloud Firestore](https://firebase.google.com/products/firestore)** - Base de datos NoSQL en tiempo real
- **[Firebase Core](https://pub.dev/packages/firebase_core)** - Configuración de Firebase

### Arquitectura

- **MVVM (Model-View-ViewModel)** - Patrón de arquitectura
- **Repository Pattern** - Capa de abstracción de datos
- **Dependency Injection** - Inyección de dependencias con Provider

---

## 📂 Estructura del Proyecto

```
ecomun/
├── lib/
│   ├── models/                    # Modelos de datos
│   │   ├── user_model.dart
│   │   ├── material_model.dart
│   │   └── request_model.dart
│   │
│   ├── services/                  # Servicios de Firebase
│   │   ├── firebase_auth_service.dart
│   │   ├── firebase_user_service.dart
│   │   ├── firebase_materials_service.dart
│   │   └── firebase_requests_service.dart
│   │
│   ├── viewmodels/                # Lógica de negocio
│   │   ├── auth_viewmodel.dart
│   │   ├── user_viewmodel.dart
│   │   ├── materials_viewmodel.dart
│   │   └── requests_viewmodel.dart
│   │
│   ├── views/                     # Pantallas de la UI
│   │   ├── login_screen.dart
│   │   ├── register_screen.dart
│   │   ├── home_screen.dart
│   │   ├── profile_screen.dart
│   │   ├── materials_info_screen.dart
│   │   └── request_form_screen.dart
│   │
│   ├── widgets/                   # Componentes reutilizables
│   │   ├── app_drawer.dart
│   │   └── material_tile.dart
│   │
│   ├── app_router.dart           # Configuración de rutas
│   ├── main.dart                 # Punto de entrada
│   └── firebase_options.dart     # Configuración Firebase
│
├── android/                       # Configuración Android
├── ios/                          # Configuración iOS
├── web/                          # Configuración Web
├── test/                         # Tests unitarios
├── pubspec.yaml                  # Dependencias
└── README.md                     # Este archivo
```

---

## 🧪 Testing

### Ejecutar Tests

```bash
# Todos los tests
flutter test

# Tests específicos
flutter test test/widget_test.dart

# Tests con cobertura
flutter test --coverage
```

---

## 📱 Capturas de Pantalla

> Añade aquí capturas de pantalla de tu aplicación

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: nueva característica'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Notas de Versión

### v1.0.0 (Diciembre 2025)

- ✅ Sistema de autenticación con Firebase
- ✅ CRUD de solicitudes de recojo
- ✅ Catálogo de materiales reciclables
- ✅ Perfil de usuario
- ✅ Estadísticas personales
- ✅ Sincronización en tiempo real

---

## 🐛 Solución de Problemas

### Error: "Firebase not initialized"

**Solución:**
```bash
flutter clean
flutter pub get
flutter run
```

### Error: "Permission denied" en Firestore

**Solución:** Verifica que las reglas de Firestore estén publicadas correctamente.

### La app no carga datos

**Solución:** 
1. Verifica tu conexión a internet
2. Revisa Firebase Console → Firestore Database
3. Ejecuta: `flutter logs` para ver errores

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👥 Autores

- **Sebastian Castro** - *Desarrollo inicial* - [GitHub](https://github.com/tu-usuario)

---

## 🙏 Agradecimientos

- Comunidad de Flutter
- Firebase Team
- Todos los contribuidores

---

## 📞 Contacto

Sebastian Castro - scastrom@ulasalle.edu.pe

Link del Proyecto: [https://github.com/tu-usuario/ecomun](https://github.com/tu-usuario/ecomun)

---

<div align="center">

**Hecho con ❤️ y ♻️ para un planeta más verde**

[⬆ Volver arriba](#️-ecomun---sistema-de-gestión-de-reciclaje)

</div>
