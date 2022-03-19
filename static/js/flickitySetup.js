var flky = new Flickity( '.car-ousel', {
    // options, defaults listed
  
    accessibility: true,
    // enable keyboard navigation, pressing left & right keys
  
    autoPlay: true,
    // advances to the next cell
    // if true, default is 3 seconds
    // or set time between advances in milliseconds
    // i.e. `autoPlay: 1000` will advance every 1 second
  
    cellAlign: 'center',
    // alignment of cells, 'center', 'left', or 'right'
    // or a decimal 0-1, 0 is beginning (left) of container, 1 is end (right)
  
    wrapAround: true,
    // at end of cells, wraps-around to first for infinite scrolling
  
    freeScroll: false,
    // enables content to be freely scrolled and flicked
    // without aligning cells
  
    contain: true,
    // will contain cells to container
    // so no excess scroll at beginning or end
    // has no effect if wrapAround is enabled
  
    pageDots: false
    // create and enable page dots
});