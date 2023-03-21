setTimeout(resizeMap, 500);

function resizeMap() {
  const map = document.getElementById("map");
  map.style.height = "360px";

  // dynamically set width in case map is juxtaposed with sidebar
  const mapContainer = document.querySelector(".mapSection");
  const mapSideBar = mapContainer?.querySelector(".mapSidebar");
  if (mapContainer && mapSideBar) {
    const mapContainerWidth = mapContainer.getBoundingClientRect().width;
    const mapSideBarWidth = mapSideBar?.getBoundingClientRect().width;
    let mapWidth;

    // from md breakpoint and smaller, map width is 100% of container
    const screenWidth = window.screen.width;
    if (screenWidth < 768) {
      mapWidth = mapContainerWidth;
    } else {
      mapWidth = mapContainerWidth - mapSideBarWidth;
    }
    map.style.width = mapWidth + "px";
  }
}

window.onresize = resizeMap;
