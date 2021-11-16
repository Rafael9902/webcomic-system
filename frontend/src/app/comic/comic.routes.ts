import { NgModule } from '@angular/core';
import { Routes, RouterModule } from "@angular/router";
import {CreateComponent} from "./components/create/create.component";

const COMIC_ROUTES: Routes = [
  {path: 'create', component: CreateComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(COMIC_ROUTES)],
  exports: [RouterModule]
})
export class ComicRoutingModule {}
