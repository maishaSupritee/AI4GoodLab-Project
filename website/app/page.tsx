//home page for website
import Image from "next/image";
import Map from "@/components/Map";

export default function Home() {
  return (
    <main className="mx-auto sm:px-10 px-5 flex flex-col">
      <header className="w-full flex items-center justify-start gap-4 py-6">
        <Image
          src="/streetscope.png"
          alt="StreetScope.ai Logo"
          width={100}
          height={100}
          className="flex-shrink-0"
        />
        <div className="flex flex-col">
          <h1 className="text-2xl sm:text-4xl font-montserrat text-[#373584] font-bold">
            StreetScope.ai
          </h1>
          <p className="text-lg sm:text-xl text-gray-700">
            A platform for data-driven urban planning
          </p>
        </div>
      </header>

      <div className="w-full h-[500px]">
        <Map />
      </div>
    </main>
  );
}
