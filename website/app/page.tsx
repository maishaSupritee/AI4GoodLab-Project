import Map from "@/components/Map";

export default function Home() {
  return (
    <main className="relative flex justify-center items-center flex-col overflow-hidden mx-auto sm:px-10 px-5">
      <div className="max-w-7xl w-full">
        <h1>StreetScope.ai</h1>
        <p>For data-driven cities</p>

        <div className="w-full h-[500px]">
          <Map />
        </div>
      </div>
    </main>
  );
}
