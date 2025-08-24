[app]
# Nombre de la app
title = Finanzas Personales
package.name = finanzas
package.domain = org.tubd
version = 0.1

# Directorio donde está tu código Python
source.dir = .

# Archivos gráficos
icon.filename = icono.png
presplash.filename = splash.png

# Archivos a incluir
source.include_exts = py,png,jpg,kv

# Librerías Python requeridas
requirements = python3,kivy

# Orientación de la pantalla
orientation = portrait

# Permisos Android
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Configuración Android
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a

# Nivel de logs
log_level = 2

# Splash y iconos extra
android.icon_background = #FFFFFF
android.icon_foreground = icono.png
android.presplash_color = #FFFFFF
