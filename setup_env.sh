#!/bin/bash
# Script para configurar el entorno virtual

set -e  # Salir si algún comando falla

echo "🔍 Verificando dependencias del sistema..."

# Verificar que Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

# Verificar que pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 no está instalado. Instalando..."
    sudo apt update && sudo apt install python3-pip python3-venv -y
fi

# Verificar que venv está disponible
if ! python3 -c "import venv" &> /dev/null; then
    echo "❌ python3-venv no está disponible. Instalando..."
    sudo apt update && sudo apt install python3-venv -y
fi

echo "✅ Dependencias del sistema verificadas"

# Eliminar entorno virtual existente si está corrupto
if [ -d "venv" ]; then
    echo "🧹 Eliminando entorno virtual existente..."
    rm -rf venv
fi

echo "🔨 Creando entorno virtual..."
python3 -m venv venv

echo "🔌 Activando entorno virtual..."
source venv/bin/activate

echo "📦 Actualizando pip..."
python -m pip install --upgrade pip

echo "📚 Instalando dependencias desde requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Dependencias instaladas correctamente"
else
    echo "⚠️  No se encontró requirements.txt"
fi

echo ""
echo "🎉 ¡Entorno configurado exitosamente!"
echo "💡 Para activarlo en el futuro usa:"
echo "   source venv/bin/activate"
echo ""
echo "🔥 Para desactivar el entorno usa:"
echo "   deactivate"
