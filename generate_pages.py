import os, re

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract head and nav
    header_match = re.search(r'(?s)(<!DOCTYPE html>.*?</nav>)', html)
    header = header_match.group(1) if header_match else ''

    def get_header_for_page(page_name):
        nav = header.replace('class="nav-link active" href="index.html"', 'class="nav-link" href="index.html"')
        nav = nav.replace(f'class="nav-link" href="{page_name}"', f'class="nav-link active" href="{page_name}"')
        return nav

    # Extract footer
    footer_match = re.search(r'(?s)(<!-- Footer -->\s*<footer class="footer">.*</html>)', html)
    footer = footer_match.group(1) if footer_match else ''

    pages = {
        'quienes-somos.html': '''
  <section class="hero-section" style="min-height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 120px 0;">
    <div class="container">
      <h1 class="hero-title serif" style="color: var(--gold-primary);">Quiénes Somos</h1>
      <p class="hero-subtitle mt-3 mx-auto text-white" style="max-width: 700px;">En Trofeón somos artesanos de la celebración. Especialistas en impresión 3D, diseño industrial y creación de piezas únicas. Transformamos los valores de tu marca en verdaderas obras de arte tangibles.</p>
    </div>
  </section>
  <section class="services-split pb-5">
    <div class="container">
      <div class="row g-5">
        <div class="col-md-6 mb-4">
          <div class="service-card" style="background: var(--navy-800); border-top: 5px solid var(--gold-primary);">
            <h4 class="serif mb-3 text-white">Nuestra Misión</h4>
             <p style="line-height: 1.8; color: var(--text-muted);">Elevar el estándar de los reconocimientos corporativos, sustituyendo las piezas genéricas por trofeos exclusivos que reflejen la grandeza y la dedicación de quienes los reciben. Queremos que cada entrega sea un momento memorable lleno de significado y admiración.</p>
          </div>
        </div>
        <div class="col-md-6 mb-4">
          <div class="service-card" style="background: var(--navy-800); border-top: 5px solid var(--gold-primary);">
            <h4 class="serif mb-3 text-white">Nuestra Visión</h4>
             <p style="line-height: 1.8; color: var(--text-muted);">Convertirnos en el aliado imprescindible de las mejores marcas y empresas, siendo reconocidos a nivel internacional como pioneros en la conceptualización y personalización dentro de la industria de galardones institucionales de alta gama.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
''',
        'contacto.html': '''
  <section class="hero-section" style="min-height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 120px 0;">
    <div class="container">
      <h1 class="hero-title serif" style="color: var(--gold-primary);">Contáctenos</h1>
      <p class="hero-subtitle mt-3 mx-auto text-white" style="max-width: 600px;">¿Tienes un proyecto en mente o quieres un presupuesto personalizado? Escríbenos y comencemos a diseñar el galardón perfecto.</p>
    </div>
  </section>
  <section class="container mt-5 mb-5">
    <div class="row g-5">
      <div class="col-lg-6">
        <form style="background: var(--navy-800); padding: 40px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div class="mb-3">
            <label class="form-label text-white">Nombre completo</label>
            <input type="text" class="form-control" placeholder="Ej. Juan Pérez">
          </div>
          <div class="mb-3">
            <label class="form-label text-white">Empresa</label>
            <input type="text" class="form-control" placeholder="Ej. Tu Empresa S.L.">
          </div>
          <div class="mb-3">
            <label class="form-label text-white">Email Corporativo</label>
            <input type="email" class="form-control" placeholder="juan@empresa.com">
          </div>
          <div class="mb-3">
            <label class="form-label text-white">Mensaje</label>
            <textarea class="form-control" rows="4" placeholder="Cuéntanos sobre tu evento..."></textarea>
          </div>
          <button type="button" class="btn-premium w-100 border-0 mt-4">Enviar Solicitud</button>
        </form>
      </div>
      <div class="col-lg-5 offset-lg-1 d-flex flex-column justify-content-center">
        <div class="mb-4">
          <h4 class="serif mb-3 text-white"><i class="bi bi-geo-alt me-2" style="color: var(--gold-primary);"></i> Sede Central</h4>
          <p class="ms-4" style="color: var(--text-muted);">Dos Hermanas, Sevilla<br>Disponibles para todo el mundo.</p>
        </div>
        <div class="mb-4">
          <h4 class="serif mb-3 text-white"><i class="bi bi-envelope me-2" style="color: var(--gold-primary);"></i> Correo Electrónico</h4>
          <p class="ms-4" style="color: var(--text-muted);">contacto@trofeon.com</p>
        </div>
        <div class="mb-4">
          <h4 class="serif mb-3 text-white"><i class="bi bi-telephone me-2" style="color: var(--gold-primary);"></i> WhatsApp</h4>
          <p class="ms-4" style="color: var(--text-muted);">+34 600 000 000</p>
        </div>
      </div>
    </div>
  </section>
''',
        'portfolio.html': '''
  <section class="hero-section" style="min-height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 120px 0;">
    <div class="container">
      <h1 class="hero-title serif" style="color: var(--gold-primary);">Nuestro Portafolio</h1>
      <p class="hero-subtitle mt-3 mx-auto text-white" style="max-width: 600px;">Explora algunas de nuestras creaciones recientes. Verdadera artesanía 3D y diseño premium.</p>
    </div>
  </section>
  <section class="portfolio-section" style="padding-top: 0;">
    <div class="container text-center">
      <div class="portfolio-grid mt-4">
        <div class="portfolio-item"><img src="assets/img/marathon_medals.png" alt="Marathon"></div>
        <div class="portfolio-item"><img src="assets/img/kids_basketball_trophy.png" alt="Basketball"></div>
        <div class="portfolio-item"><img src="assets/img/esports_trophy.png" alt="E-Sports"></div>
        <div class="portfolio-item"><img src="assets/img/collab_trophy.png" alt="Collab"></div>
        <div class="portfolio-item"><img src="assets/img/clients_trophy.png" alt="Clients"></div>
        <div class="portfolio-item"><img src="assets/img/products_trophy.png" alt="Products"></div>
      </div>
    </div>
  </section>
''',
        'presupuesto.html': '''
  <section class="hero-section" style="min-height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 120px 0;">
    <div class="container">
      <h1 class="hero-title serif" style="color: var(--gold-primary);">Solicitar Presupuesto</h1>
      <p class="hero-subtitle mt-3 mx-auto text-white" style="max-width: 600px;">Rellena el siguiente formulario para que podamos estimar los costes de tu proyecto.</p>
    </div>
  </section>
  <section class="container mt-5 mb-5 pb-5">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <form style="background: var(--navy-800); padding: 40px; border-radius: 12px; border: 1px solid var(--glass-border);">
          <div class="row mb-3">
             <div class="col-md-6">
                <label class="form-label text-white">Tipo de Trofeo</label>
                <select class="form-select"><option>Listos del Catálogo</option><option>Proyecto Exclusivo</option></select>
             </div>
             <div class="col-md-6 mt-3 mt-md-0">
                <label class="form-label text-white">Cantidad Aproximada</label>
                <input type="number" class="form-control" value="1">
             </div>
          </div>
          <div class="mb-3">
            <label class="form-label text-white">Describe tu idea</label>
            <textarea class="form-control" rows="4"></textarea>
          </div>
          <button type="button" class="btn-premium w-100 border-0 mt-4">Solicitar Cita</button>
        </form>
      </div>
    </div>
  </section>
''',
        'blog.html': '''
  <section class="hero-section" style="min-height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 120px 0;">
    <div class="container">
      <h1 class="hero-title serif" style="color: var(--gold-primary);">El Blog de Trofeón</h1>
      <p class="hero-subtitle mt-3 mx-auto text-white" style="max-width: 600px;">Novedades, inspiración y el detrás de escena de nuestras creaciones en 3D.</p>
    </div>
  </section>
  <section class="container mt-5 mb-5 pb-5">
    <div class="row g-4" id="blog-posts-container">
      <!-- Los posts del blog irán aquí -->
      <div class="col-12 text-center my-5">
        <h3 style="color: var(--text-muted);">Próximamente nuevos artículos...</h3>
      </div>
    </div>
  </section>
''',
        'catalogo.html': '''
  <section class="hero-section" style="min-height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 120px 0;">
    <div class="container">
      <h1 class="hero-title serif" style="color: var(--gold-primary);">Catálogo de Trofeos</h1>
      <p class="hero-subtitle mt-3 mx-auto text-white" style="max-width: 600px;">Explora nuestras piezas listas para personalizar.</p>
    </div>
  </section>
  <section class="container mb-5 pb-5 portfolio-section" style="padding-top: 0;">
    <div class="portfolio-grid mt-4">
      <div class="portfolio-item position-relative">
        <img src="assets/img/catalog-trophy.png" alt="Trofeo">
        <div class="position-absolute bottom-0 start-0 w-100 p-3" style="background: rgba(5,11,20,0.8);">
          <h5 class="text-white mb-0 serif">Trofeo Ejecutivo</h5>
        </div>
      </div>
      <div class="portfolio-item position-relative">
        <img src="assets/img/clients_trophy.png" alt="Trofeo">
        <div class="position-absolute bottom-0 start-0 w-100 p-3" style="background: rgba(5,11,20,0.8);">
          <h5 class="text-white mb-0 serif">Galardón Innovación</h5>
        </div>
      </div>
      <div class="portfolio-item position-relative">
        <img src="assets/img/collab_trophy.png" alt="Trofeo">
        <div class="position-absolute bottom-0 start-0 w-100 p-3" style="background: rgba(5,11,20,0.8);">
          <h5 class="text-white mb-0 serif">Medalla Corporativa</h5>
        </div>
      </div>
      <div class="portfolio-item position-relative">
        <img src="assets/img/products_trophy.png" alt="Trofeo">
        <div class="position-absolute bottom-0 start-0 w-100 p-3" style="background: rgba(5,11,20,0.8);">
          <h5 class="text-white mb-0 serif">Trofeo Producto Escala</h5>
        </div>
      </div>
    </div>
  </section>
'''
    }

    for page, content in pages.items():
        if header and footer:
            full_html = get_header_for_page(page) + content + footer
            with open(page, 'w', encoding='utf-8') as f:
                f.write(full_html)
            print(f"Created {page}")
        else:
            print("Failed to extract head or footer", bool(header), bool(footer))

except Exception as e:
    print("Error:", e)
