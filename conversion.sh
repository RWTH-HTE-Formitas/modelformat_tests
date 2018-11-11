if ! [ -x "$(command -v obj2gltf)" ]; then
  echo '>> Error: obj2gltf is not installed. download node.js and then run' >&2
  echo '>> npm install -g obj2gltf'
  exit 1
fi

for format in "obj2gltf" "dae2gltf" "collada" "obj"
  do
    if [ ! -d "data/$format" ]; then
      mkdir -p "data/$format";
    fi
  done

for a in data/IFC/*.ifc ; do
    d=$(basename $a .ifc)
    echo "converting $d"
    ./Binaries/IfcConvert data/IFC/$d.ifc  data/collada/$d.dae
    ./Binaries/COLLADA2GLTF-bin -i data/collada/$d.dae -o data/dae2gltf/$d.gltf

    ./Binaries/IfcConvert data/IFC/$d.ifc data/obj/$d.obj
    obj2gltf -i data/obj/$d.obj -o data/obj2gltf/$d.gltf 
done
