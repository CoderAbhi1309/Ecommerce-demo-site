import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DatabindingComponent } from './databinding/databinding.component';
import { LandingComponent } from './landing/landing.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import {HeaderComponent} from './header/header.component'
import { FooterComponent } from './footer/footer.component';
import { ProfileComponent } from './profile/profile.component';
import { WomenComponent } from './women/women.component';
import { MenComponent } from './men/men.component';
import {CarouselComponent} from './carousel/carousel.component'

const routes: Routes = [
{
  path: 'signup',
  component: SignupComponent
},
{  
  path:'login',
  component:LoginComponent
  },
{
  path: 'landing',
  component: LandingComponent
},
{
  path: 'databinding',
  component: DatabindingComponent
},
{
  path: 'header',
  component: HeaderComponent
},
{
  path: 'footer',
  component: FooterComponent
},
{
  path: 'profile',
  component: ProfileComponent
},
{
  path: 'women',
  component: WomenComponent
},
{
  path: 'men',
  component: MenComponent
},
{  
  path:'carousel',
  component:CarouselComponent
  },
{
  path:'',
  redirectTo : '/landing',
  pathMatch: 'full'
},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }