import Map from "@/components/Map";

export default function Home() {
  return (
    <main className="relative flex justify-center items-center flex-col overflow-hidden mx-auto sm:px-10 px-5">
      <div className="max-w-7xl w-full text-center flex flex-col justify-center items-center gap-5 my-10">
        <h1 className="text-4xl sm:text-6xl font-bold text-purple-200 my-5">
          StreetScope.ai
        </h1>
        <p className="text-lg sm:text-xl text-gray-700">
          A platform for data-driven urban planning
        </p>
      </div>

      <div className="w-full h-[500px]">
        <Map />
      </div>
    </main>
  );
}
