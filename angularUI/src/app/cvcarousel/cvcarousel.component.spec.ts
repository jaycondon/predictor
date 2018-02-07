import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CvcarouselComponent } from './cvcarousel.component';

describe('CvcarouselComponent', () => {
  let component: CvcarouselComponent;
  let fixture: ComponentFixture<CvcarouselComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CvcarouselComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CvcarouselComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
