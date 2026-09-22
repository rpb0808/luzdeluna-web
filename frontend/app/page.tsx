const SERVICIOS = [
  {
    nombre: "Equinoterapia",
    descripcion: "Estimulacion y terapia asistida con caballos.",
  },
  {
    nombre: "Salto",
    descripcion: "Clases individuales y grupales de salto de obstaculos.",
  },
  {
    nombre: "Adiestramiento",
    descripcion: "Doma clasica, para todos los niveles.",
  },
  {
    nombre: "Vaulting",
    descripcion: "Gimnasia sobre el caballo, en movimiento.",
  },
];

export default function Home() {
  return (
    <main>
      <section className="relative flex min-h-[70vh] items-end bg-luna-verde px-6 py-16 text-white sm:px-12">
        <div className="max-w-2xl">
          <p className="mb-2 font-serif italic text-luna-dorado">
            Bienvenidos a
          </p>
          <h1 className="font-serif text-5xl leading-tight sm:text-6xl">
            Luz de Luna Centro Ecuestre
          </h1>
          <p className="mt-4 text-lg text-white/80">
            Club Hipico - La Molina, Lima. Equinoterapia, salto, adiestramiento
            y vaulting.
          </p>
          <a
            href="#reservar"
            className="mt-8 inline-block rounded-full bg-luna-dorado px-6 py-3 font-medium text-luna-texto transition hover:opacity-90"
          >
            Reserva una clase
          </a>
        </div>
      </section>

      <section className="px-6 py-16 sm:px-12">
        <h2 className="font-serif text-3xl">Nuestras disciplinas</h2>
        <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {SERVICIOS.map((s) => (
            <div key={s.nombre} className="rounded-lg border border-luna-verde/10 p-6">
              <h3 className="font-serif text-xl text-luna-verde">{s.nombre}</h3>
              <p className="mt-2 text-sm text-luna-texto/70">{s.descripcion}</p>
            </div>
          ))}
        </div>
      </section>

      <section id="reservar" className="bg-luna-verde/5 px-6 py-16 sm:px-12">
        <h2 className="font-serif text-3xl">Reserva tu clase</h2>
        <p className="mt-2 max-w-xl text-luna-texto/70">
          Este formulario es un punto de partida: hoy guarda la reserva en el
          backend (en memoria). El siguiente paso es conectarlo a la base de
          datos y agregar el pago online.
        </p>
      </section>
    </main>
  );
}
