import {Component, OnInit} from '@angular/core';
import * as $ from 'jquery';

@Component({
  selector: 'app-cvcarousel',
  templateUrl: './cvcarousel.component.html',
  styleUrls: ['./cvcarousel.component.css']
})

export class CvcarouselComponent implements OnInit {

  constructor() {}

  moveUsingIndicator(event) {
    console.log(event);
  }

  ngOnInit() {

    window.setInterval(function() {
      moveCorousel('right');
    }, 7000);

    // Enable Carousel Indicators
    $('.carousel-control-next').on('click', function() {
      moveCorousel('right');
    });

    // Enable Carousel Controls
    $('.carousel-control-prev').on('click', function() {
      moveCorousel('left');
    });

    function moveCorousel(direction) {
      const activeCarouselItem = $('.carousel-item.active');
      const carouselItemToMoveTo = direction === 'left' ? activeCarouselItem.prev() : activeCarouselItem.next();
      activeCarouselItem.removeClass('active');
      if (carouselItemToMoveTo.length === 0) {
        const carouselChildren = $('.carousel-inner').children();
        direction === 'left' ? carouselChildren.last().addClass('active') : carouselChildren.first().addClass('active');
      } else {
        direction === 'left' ? activeCarouselItem.prev().addClass('active') : activeCarouselItem.next().addClass('active');
      }
      $('.carousel-indicators > li').removeClass('active');
      $('.carousel-indicators > li:eq(' + $('.carousel-item.active').index() + ')').addClass('active');
    }

  }
}
