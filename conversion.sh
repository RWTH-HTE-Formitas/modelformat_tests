if ! [ -x "$(command -v obj2gltf)" ] || [ -x "$(command -v gltf-pipeline)" ] ]; then
  echo '>> Install dependencies: download node.js and run' >&2
  echo '>> npm install -g obj2gltf'
  echo '>> npm install -g gltf-pipeline'
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
    gltf-pipeline -i data/dae2gltf/$d.gltf -o data/dae2gltf/$d.opt.gltf

    ./Binaries/IfcConvert data/IFC/$d.ifc data/obj/$d.obj
    obj2gltf -i data/obj/$d.obj -o data/obj2gltf/$d.gltf
    gltf-pipeline -i data/obj2gltf/$d.gltf -o data/obj2gltf/$d.opt.gltf
done
