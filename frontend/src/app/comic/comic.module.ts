import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ComicService } from "./services/comic.service";
import { CreateComponent } from './components/create/create.component';
import { ComicRoutingModule } from "./comic.routes";
import { ReactiveFormsModule } from '@angular/forms';
import {RouterModule} from '@angular/router';


@NgModule({
  declarations: [
    CreateComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterModule
  ],
  exports: [ComicRoutingModule],
  providers: [ComicService]
})
export class ComicModule { }
