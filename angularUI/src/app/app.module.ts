import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { PersonalinformationComponent } from './personalinformation/personalinformation.component';
import { WorkexperienceComponent } from './workexperience/workexperience.component';
import { EducationComponent } from './education/education.component';
import { CvcarouselComponent } from './cvcarousel/cvcarousel.component';


@NgModule({
  declarations: [
    AppComponent,
    PersonalinformationComponent,
    WorkexperienceComponent,
    EducationComponent,
    CvcarouselComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
