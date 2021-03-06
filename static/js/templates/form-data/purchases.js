// Get form-purchases data
async function FormPurchasesData(user) {
    this.template = {
        showDetails: async (user) => {
            
            const ETIQUETAA = document.getElementsByClassName('secondary-btn')[0];
            const FORMCOMPRA = document.querySelector('#formPurchase');
            let inputProducto = document.getElementById('producto');
            let inputCantidad = document.getElementById('cantidad');
            let inputTotal = document.getElementById('total');
            let inputProveedor = document.getElementById('proveedor');
            let inputIdProveedor = document.getElementById('idProveedor');
            let inputStock = document.getElementById('stock');
            async function getData(url) {
                const response = await fetch(url);
                const data = await response.json();
                return data;
            }
            setAttributes(ETIQUETAA, {
                href: '/purchases/',
            });
            const products = await getData('http://127.0.0.1:8000/fetch_products/');
            const providers = await getData('http://127.0.0.1:8000/categories_and_providers/');
            let buyers;
            if (getUserType(user) == 0 || getUserType(user) == 1) {
                buyers = await getData('http://127.0.0.1:8000/fetch_buyers/');
                ;
            }
            else if (getUserType(user) == 2) {
                buyers = user;
            }
            let idProduct;
            let prod;
            function addOptions(selectName, data) {
                selectElement = document.getElementById(selectName);
                for (let i = 0; i < data.length; i++) {
                    const optionElement = document.createElement('option');
                    if (i === 0) {
                        setAttributes(optionElement, {
                            value: data[i].key,
                            selected: true
                        });
                        idProduct = data[i].key;
                        prod = products.products.find(x => x.key === data[i].key);
                    }
                    else {
                        setAttributes(optionElement, {
                            value: data[i].key,
                        });
                    }
                    optionElement.innerHTML = data[i].name;
                    selectElement.appendChild(optionElement);
                }
            }
            function addOptionsUsers(selectName, data) {
                selectElement = document.getElementById(selectName);
                for (let i = 0; i < data.length; i++) {
                    const optionElement = document.createElement('option');
                    if (i === 0) {
                        setAttributes(optionElement, {
                            value: data[i].key,
                            selected: true
                        });
                    }
                    else {
                        setAttributes(optionElement, {
                            value: data[i].key,
                        });
                    }
                    optionElement.innerHTML = data[i].name;
                    selectElement.appendChild(optionElement);
                }
            }
            if (getUserType(user) == 0 || getUserType(user) == 1) {
                addOptionsUsers('vendedor', buyers.buyers);
            }
            else if (getUserType(user) == 2) {
                let vend = document.getElementById('vendedor');
                vend.disabled = true;
                const optionElement = document.createElement('option');
                setAttributes(optionElement, {
                    value: user.emp_key,
                });
                optionElement.innerHTML = `${user.first_name} ${user.last_name}`;
                vend.appendChild(optionElement);
            }
            addOptions('producto', products.products);
            addOptionsUsers('proveedor', providers.providers);
            setAttributes(document.getElementById('cantidad'), {
                min: 1,
            });
            let proveedor = await getData(`http://127.0.0.1:8000/fetch_provider/${prod.provider}/`);
            inputProveedor.value = proveedor.provider.name;
            inputIdProveedor.value = proveedor.provider.provider_key;
            let stock = await getData(`http://127.0.0.1:8000/fetch_product_stock/${idProduct}/`);
            inputStock.value = stock.stock.amount;
            inputProducto.addEventListener('change', async (e) => {
                prod = products.products.find(x => x.key === e.target.value);
                inputCantidad.value = 1;
                inputTotal.value = prod.price;
                proveedor = await getData(`http://127.0.0.1:8000/fetch_provider/${prod.provider}/`);
                inputProveedor.value = proveedor.provider.name;
                inputIdProveedor.value = proveedor.provider.provider_key;
                stock = await getData(`http://127.0.0.1:8000/fetch_product_stock/${prod.key}/`);
                inputStock.value = stock.stock.amount;
            });
            inputCantidad.addEventListener('change', async (e) => {
                totalPrecio = prod.price * inputCantidad.value;
                inputTotal.value = totalPrecio;
            });
            FORMCOMPRA.addEventListener('submit', async (e) => {
                e.preventDefault();
                if (document.getElementById('producto').value !== '' && document.getElementById('cantidad').value !== '' && document.getElementById('total').value !== '' && document.getElementById('proveedor').value !== '' && document.getElementById('vendedor').value !== '') {
                    const form = new FormData();
                    form.append('product', document.getElementById('producto').value);
                    form.append('amount', document.getElementById('cantidad').value);
                    form.append('total', document.getElementById('total').value);
                    form.append('provider', document.getElementById('idProveedor').value);
                    form.append('employee', document.getElementById('vendedor').value);
                    try {
                        console.log('si');
                        const data = await mandarData('http://127.0.0.1:8000/buy_product/', form);
                        if (data.status === 200) {
                            showModal('Compra registrada <br> correctamente', 'fas fa-check-circle', '/purchases/');
                        }
                        else {
                            showModal('Ocurrió un error, <br> intenta de nuevo', 'fas fa-times',);
                        }
                    }
                    catch (error) {
                        console.log(error);
                    }
                }
                else {
                    showModal('Llena todos los <br>campos', 'fas fa-times',);
                }
            });
        }
    };
    return this.template;
}
