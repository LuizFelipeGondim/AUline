
function CategoriaAnimal(){
    const categorias = JSON.parse(document.getElementById('categorias').textContent);
    const ids = JSON.parse(document.getElementById('ids').textContent);
    for(let i = 0; i < ids.length; i++){
        if (categorias[ids[i]] == 'Encontrado'){
            document.getElementById(ids[i]).style.border="2px solid #5eed5e";
            document.getElementById(ids[i]).style.borderRadius="10px";
        } else if (categorias[ids[i]] == 'Perdido'){
            document.getElementById(ids[i]).style.border="2px solid #ed8787";
            document.getElementById(ids[i]).style.borderRadius="10px";
        } else if (categorias[ids[i]] == 'Para Adoção'){
            document.getElementById(ids[i]).style.border="2px solid #3fbcdb";
            document.getElementById(ids[i]).style.borderRadius="10px";
        } else if (categorias[ids[i]] == 'Adotado'){
            document.getElementById(ids[i]).style.border="2px solid #9b228b";
            document.getElementById(ids[i]).style.borderRadius="10px";
        }
    }
    
}

CategoriaAnimal();